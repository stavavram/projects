var kontainer = require('kontainer-di');

var config = require('./config/default.json');
var cache = require('./services/cache/redisCache').RedisCache;
var storage = require('./services/storage').Storage;

kontainer.register('config', [], config);
kontainer.register('cache', ['config'], cache);
kontainer.register('storage', [], storage);

//export the configured DI container
module.exports = kontainer;