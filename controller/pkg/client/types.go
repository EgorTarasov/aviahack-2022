package client

import "net/http"

type Client struct {
	client *http.Client
}

type ImageExplorerPreview struct {
	Image string      `json:"image"`
	Avg   interface{} `json:"avg"`
}

type ActivityItem struct {
	Screen      string                 `json:"screen"`
	Url         string                 `json:"url"`
	Id          string                 `json:"id"`
	Slug        string                 `json:"slug"`
	Title       string                 `json:"title"`
	Description string                 `json:"description"`
	Preview     []ImageExplorerPreview `json:"image_explore_preview"`
	City        []string               `json:"city"`
	CityObject  interface{}            `json:"cityObject"`
	Region      []string               `json:"region"`
	TagsIds     []string               `json:"tags_ids"`
	Price       string                 `json:"price"`
	Sort        int                    `json:"sort"`
	IsCanBuy    string                 `json:"is_can_buy"`
}

type PriceRange struct {
	Min int `json:"min"`
	Max int `json:"max"`
}

type PriceBucket struct {
	Min   int `json:"min"`
	Max   int `json:"max"`
	Count int `json:"count"`
}

type Tag struct {
	Id      string                 `json:"id"`
	Slug    string                 `json:"slug"`
	Title   string                 `json:"title"`
	Images  []ImageExplorerPreview `json:"images"`
	IconPin []interface{}          `json:"icon_pin"`
}

type City struct {
	Id    string `json:"id"`
	Slug  string `json:"slug"`
	Title string `json:"title"`
}

type Region struct {
	Id    string `json:"id"`
	Slug  string `json:"slug"`
	Title string `json:"title"`
}

type Option struct {
	Title string `json:"title"`
	Slug  string `json:"slug"`
	TagId string `json:"tag_id"`
}

type Filter struct {
	Title   string   `json:"title"`
	Name    string   `json:"name"`
	ByValue bool     `json:"by_value"`
	Options []Option `json:"options"`
}

type Meal struct {
	Name string `json:"name"`
	Tag  string `json:"tag"`
}

type Event struct {
	Id     string                 `json:"id"`
	Slug   string                 `json:"slug"`
	Title  string                 `json:"title"`
	Images []ImageExplorerPreview `json:"images"`
}

type CategoryStruct struct {
	Page           int            `json:"page"`
	PageSize       int            `json:"pageSize"`
	Total          int            `json:"total"`
	Items          []ActivityItem `json:"items"`
	PriceRange     PriceRange     `json:"price_range"`
	PriceBuckets   []PriceBucket  `json:"price_buckets"`
	Tags           []Tag          `json:"tags"`
	Cities         []City         `json:"cities"`
	EventTypes     []Event        `json:"event_types"`
	Regions        []Region       `json:"regions"`
	ExcursionTypes []interface{}  `json:"excursion_types"`
	Filters        []Filter       `json:"filters"`
	Raitings       []float64      `json:"ratings"`
	// Meals          []Meal         `json:"meal"`
}

type Coordinate struct {
	Longitude float64 `json:"lng"`
	Latitude  float64 `json:"lat"`
}
type Place struct {
	Id            string                 `json:"id"`
	Title         string                 `json:"title"`
	Slug          string                 `json:"slug"`
	Description   string                 `json:"description"`
	Address       string                 `json:"address"`
	GoogleAddress string                 `json:"google_address"`
	Coordinates   Coordinate             `json:"coordinates"`
	Images        []ImageExplorerPreview `json:"images"`
	Preview       []ImageExplorerPreview `json:"image_explore_preview"`
	Detailed      []ImageExplorerPreview `json:"image_detailed_page_main"`
	TagsIds       []string               `json:"tags_ids"`
	MetroIds      []string               `json:"metro_ids"`
	DIstrictIds   []string               `json:"district_ids"`
	// working_time
}

// type TagStruct struct {
// 	Events []Tag `json:"tags"`
// }
