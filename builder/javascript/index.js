class UrlBuilder {

    setProtocol(protocol) {
        this.protocol = protocol
        return this
    }

    setHost(host) {
        this.host = host
        return this
    }

    setPort(port) {
        this.port = port
        return this
    }

    build() {
        return `${this.protocol}://${this.host}:${this.port}`
    }
}

const url = new UrlBuilder()
    .setProtocol('http')
    .setHost('localhost')
    .setPort('3000')
    .build() 

console.log(url) // http://localhost:3000