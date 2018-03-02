package main

import (
	"fmt"
	"log"
	"net/http"
	"time"
)

func indexHandler(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusOK)
	w.Header().Set("Content-Type", "text/plain")
	w.Write([]byte(fmt.Sprintf("Greetings!\nCurrent time: %s", time.Now())))
}

const serverAddr = "localhost:8080"

func main() {
	http.HandleFunc("/", indexHandler)

	svr := &http.Server{
		Addr:         serverAddr,
		ReadTimeout:  time.Second,
		WriteTimeout: time.Second,
	}

	log.Printf("Greeter: Serving %s", serverAddr)
	err := svr.ListenAndServe()
	if err != nil {
		log.Fatalf("fatal error: cannot start the server: %v", err)
		return
	}
}
