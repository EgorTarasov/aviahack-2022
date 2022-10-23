package utils

import (
	"bytes"
	"log"

	"github.com/joho/godotenv"
)

func GetEnv() *Env {
	log.Println("PROCESSING .env file")
	envs, err := godotenv.Read(ENVPATH)

	if err != nil {
		log.Fatalf("ERROR During loading .env file: %s", err)
	}

	for key, value := range envs {
		if bytes.Contains([]byte(key), []byte("\xef\xbb\xbf")) {
			newkey := bytes.Trim([]byte(key), "\xef\xbb\xbf")
			delete(envs, key)
			envs[string(newkey)] = value
		}
	}
	env := Env{
		DatabaseUrl: envs["DATABASE_URL"],
	}

	return &env
}
