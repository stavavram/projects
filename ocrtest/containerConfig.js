var kontainer = require('kontainer-di');

var config = require('./config/default.json');
var cache = require('./services/cache/redisCache').RedisCache;
var archive = require('./services/archive/elasticArchive').ElasticArchive;
var storage = require('./services/storage').Storage;
var ocrConvertor = require('./services/ocrConvertor').OCRConvertor

kontainer.register('config', [], config);
kontainer.register('storageConfig', [], config.storage);
kontainer.register('archiveConfig', [], config.archive);
kontainer.register('cache', ['config'], cache);
kontainer.register('archive', ['archiveConfig'], archive);
kontainer.register('storage', ['storageConfig'], storage);
kontainer.register('ocrconvertor', ['config'], ocrConvertor);

module.exports = kontainer;