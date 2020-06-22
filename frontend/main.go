package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

// Backend struct
type Backend struct {
	Code    int    `json:"code"`
	Message string `json:"message"`
}

func main() {
	var respAPI Backend

	router := gin.Default()
	router.LoadHTMLGlob("templates/*")
	router.GET("/", func(c *gin.Context) {
		client := &http.Client{Timeout: time.Second * 5}
		req, _ := http.NewRequest(http.MethodGet, "http://localhost:8081/info", nil)
		resp, err := client.Do(req)

		if err != nil {
			c.HTML(http.StatusServiceUnavailable, "view.tmpl", gin.H{
				"title": fmt.Sprintf("%s", err),
			})
		}

		defer resp.Body.Close()

		err = json.NewDecoder(resp.Body).Decode(&respAPI)

		if err != nil {
			c.HTML(http.StatusServiceUnavailable, "view.tmpl", gin.H{
				"title": fmt.Sprintf("%s", err),
			})
		}

		c.HTML(http.StatusOK, "view.tmpl", gin.H{
			"title": fmt.Sprintf("%s", respAPI.Message),
		})
	})
	router.Run(":8080")
}
