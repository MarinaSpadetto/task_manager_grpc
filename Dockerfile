# Use uma imagem base leve do Golang
FROM golang:1.18-alpine as builder

# Configure o diretório de trabalho dentro do contêiner
WORKDIR /app

# Clone o repositório do Evans
RUN apk add --no-cache git
RUN git clone https://github.com/ktr0731/evans.git .

# Compilar o Evans
RUN go build -o /bin/evans

# Use uma imagem mínima do Alpine como imagem base
FROM alpine:latest

# Copiar o executável Evans da imagem do builder
COPY --from=builder /bin/evans /bin/evans

# Definir o comando padrão ao iniciar o contêiner
ENTRYPOINT ["/bin/evans"]
