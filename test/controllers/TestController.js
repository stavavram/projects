var container = require('../containerConfig');
var ocrConvertor = container.get("ocrconvertor")

module.exports.uploadFile = function (req, res, next) {
    let pathResults = req.upload.files.map(file=> file.path);
    res.setHeader("Content-Type", "application/json")
    res.statusCode = 201;
    res.end(JSON.stringify(pathResults));
}

module.exports.extractTextFromFile = async function (req, res, next) {
    let path = req.swagger.params.filepath.value;
    res.setHeader("Content-Type", "application/text");
    try{
        let textRes = await ocrConvertor.convertImageToText(path);
        res.statusCode = 200;
        res.end(textRes);
    }
    catch (err){
        res.statusCode = 500;
        res.end(err.message);
    }
}
