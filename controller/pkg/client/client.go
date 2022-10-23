package client

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"

	_ "github.com/lib/pq"
)

// Awaiting api url  e.g. /cmsapi/regions/...
// query map[string][]string with additional params
// Need to check for error code if something fails
func (r Client) Get(apiUrl string, params map[string][]string, body io.Reader, header io.Reader) ([]byte, error) {
	req, err := http.NewRequest(http.MethodGet, BaseUrl+apiUrl, body)
	if err != nil {
		return nil, fmt.Errorf("error: %w", err)
	}
	if len(params) > 0 {
		q := req.URL.Query()
		for key, value := range params {
			q.Add(key, value[0])
		}
		fmt.Println(q.Encode())
		req.URL.RawQuery = q.Encode()
	}
	fmt.Println(req.URL.String())
	resp, err := r.client.Do(req)
	if err != nil {
		return nil, err
	}

	defer resp.Body.Close()
	if resp.StatusCode == http.StatusOK {
		bodyBytes, err := io.ReadAll(resp.Body)
		if err != nil {
			return nil, err //fmt.Errorf("got %d Status Code. Error: %w", resp.StatusCode, err)
		}
		log.Println("Error is: ", err)
		return bodyBytes, err
	} else {
		return nil, err
	}

}

func (r Client) Post(apiUrl string, body io.Reader, header io.Reader) ([]byte, int) {

	req, err := http.NewRequest(http.MethodPost, BaseUrl+apiUrl, body)
	if err != nil {
		log.Println("ERROR: ", err)
	}

	resp, err := r.client.Do(req)
	if err != nil {
		log.Println("ERROR: ", err)
	}

	defer resp.Body.Close()
	if resp.StatusCode == http.StatusOK {
		bodyBytes, err := io.ReadAll(resp.Body)
		if err != nil {
			log.Println("ERROR: ", err)

			return nil, resp.StatusCode
		}
		return bodyBytes, resp.StatusCode
	} else {
		return nil, resp.StatusCode
	}
}

func (r Client) GetCategory(params map[string][]string) (CategoryStruct, error) {
	var gotCategory CategoryStruct
	data, err := r.Get(CatalogApi, params, nil, nil)
	if err != nil {
		log.Fatalf(err.Error())
		return CategoryStruct{}, err
	}
	nerr := json.Unmarshal(data, &gotCategory)

	if nerr != nil {
		log.Fatalf(nerr.Error())
		return CategoryStruct{}, err
	}
	gotCategory.Raitings = nil
	return gotCategory, err
}

// func (r Client) getTags(params map[string][]string) {
// 	var tg TagStruct
// 	data, err := r.Get(TagsApi, nil, nil, nil)
// 	if err != nil {
// 		log.Println(err)
// 		return
// 	}
// 	nerr := json.Unmarshal(data, &tg)

// 	if nerr != nil {
// 		log.Fatalf(nerr.Error())
// 		return TagStruct{}, err
// 	}
// 	return tg, err
// }

// 629dd05749df2290f21f9881
func (r Client) GetPlace(params map[string][]string) (Place, error) {
	var plc Place
	data, err := r.Get(TagsApi, params, nil, nil)
	if err != nil {
		log.Println(err)
	}
	nerr := json.Unmarshal(data, &plc)
	if nerr != nil {
		log.Fatalf(nerr.Error())
	}
	return plc, err
}

func NewClient() *Client {
	cl := Client{
		client: &http.Client{},
	}
	return &cl
}
