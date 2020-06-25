package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

func main() {
	t := time.Now()

	client := &http.Client{Timeout: time.Second * 5}
	req, _ := http.NewRequest(http.MethodGet, fmt.Sprintf("http://numbersapi.com/%d/%d/date", t.Month(), t.Day()), nil)
	resp, err := client.Do(req)

	if err != nil {
		fmt.Println(err)
	}

	defer resp.Body.Close()

	router := gin.Default()

	content, _ := ioutil.ReadAll(resp.Body)
	router.GET("/info", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"code":    http.StatusOK,
			"message": fmt.Sprintf("%s", content),
		})
	})

	router.Run(":8080")
}
