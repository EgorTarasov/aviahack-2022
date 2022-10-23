FROM golang:alpine as builder

ENV HTTPS_PROXY=http://proxy.russpass.dev:3128
ENV HTTP_PROXY=http://proxy.russpass.dev:3128
ENV https_proxy=http://proxy.russpass.dev:3128
ENV http_proxy=http://proxy.russpass.dev:3128

WORKDIR /build/
COPY go.mod .
COPY go.sum .
RUN go mod download
COPY . /build/
RUN go build -o main ./cmd/main

FROM alpine
COPY --from=builder /build/main /app/
WORKDIR /app
CMD ["./main"]