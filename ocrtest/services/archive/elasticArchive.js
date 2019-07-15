var Redis = require('elasticsearch');

module.exports.ElasticArchive = class ElasticArchive {
    constructor(config){
        this.config = config;
        this.client = new elasticsearch.Client({
            host: ''
        })
    }
}