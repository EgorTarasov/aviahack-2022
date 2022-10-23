package server

import (
	"fmt"
	"log"
	"net/http"
	"strconv"

	"mmm/pkg/client"
	"mmm/pkg/scheduler"

	"github.com/gin-gonic/gin"
)

func API() error {
	gin.SetMode(gin.ReleaseMode)
	r := gin.Default()

	// api := r.Group("/api")
	r.GET("/catalog", getCatalogHandler)
	r.POST("/save_event", postEvent)
	r.GET("/health", healthHandler)
	r.GET("/flights", getFlights)
	// api.GET("/proxy/env", getEnvHandler)

	return r.Run(":" + strconv.Itoa(port))
}

func postEvent(ctx *gin.Context) {
	var event Event
	ctx.BindJSON(&event)
	ctx.JSON(200, gin.H{"ids": "123"})
}

func getPlace(ctx *gin.Context) {
	cl := client.NewClient()
	s, err := cl.GetPlace(ctx.Request.URL.Query())
	if err != fmt.Errorf("%w", nil) {
		log.Println(err)
	}
	ctx.JSON(http.StatusOK, s)

}

func healthHandler(ctx *gin.Context) {
	ctx.Status(http.StatusOK)
}

func getFlights(ctx *gin.Context) {
	flight, err := scheduler.SelectFlights()
	if err != nil {
		log.Println(err)
	}
	ctx.JSON(http.StatusOK, flight)
}

// func mainHandler(ctx *gin.Context) {

// }

// Эта функция является враппером над 	https://api.stage01.russpass.dev/cmsapi/catalog
func getCatalogHandler(ctx *gin.Context) {
	cl := client.NewClient()
	s, err := cl.GetCategory(ctx.Request.URL.Query())
	if err != fmt.Errorf("%w", nil) {
		log.Println(err)
	}
	ctx.JSON(http.StatusOK, s)

}
