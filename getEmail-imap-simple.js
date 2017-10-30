// https://stackoverflow.com/questions/31213294/telegram-api-send-messages-with-php-or-javascript#31213509

var imaps = require('imap-simple');
const fs = require( 'fs');

//var tradeData = fs.readFileSync( tradeFile, 'UTF-8');
//fs.writeFileSync( writeFile, writeData, 'UTF-8');
//const CURRENCYFIELD = 'CUR';


const GOLDEN_ECHO = 'golden-echo';
const COLOR_CHANGE = 'COLOR_CHANGE';
const COLOR_RETURN = 'COLOR_RETURN';
const E240 = 'e240';
const UNSEEN = 'UNSEEN';
const INBOX = 'INBOX';
const HEADER = 'HEADER';
const TEXT = 'TEXT';

var config = {
	imap: {
		user: 'gcfxalerts@gmail.com',
		password: 'm40K3NioJsB8',
		host: 'imap.gmail.com',
		port: 993,
		tls: true,
		authTimeout: 3000
	}
};

imaps.connect(config).then(function (connection) {

	return connection.openBox(INBOX).then(function () {
		var searchCriteria = [
			UNSEEN
		];

		var fetchOptions = {
			bodies: [HEADER, TEXT],
			markSeen: false
		};

		return connection.search(searchCriteria, fetchOptions).then(function (results) {
			for ( var i1 in results) {
				for ( i2 in results[i1].parts) {
					var email = results[i1].parts[i2];
					if (email.which === HEADER) {
						var emailDate = email.body.date[0];
					}
					if ( email.which === TEXT && email.body.substr(0,5) === 'Alert') {
						var message = getSignalFromMessage( email.body);
						var jsonString = extractJSONfromMessage( email.body, message);
						console.log( jsonString);
					}
				}
			}
			// var msgs = results.map(function (res) {
			//     return res.parts.filter(function (part) {
			//         return part.which === 'TEXT';
			//     })[0].body;
			// });

			// console.log(msgs);
		});
	});
});

function getSignalFromMessage( body) {
	let sp = body.indexOf( '| Study:') + 9;
	let ep = body.indexOf( ' | ', sp);
	return body.substr( sp, (ep-sp));
}

function extractJSONfromMessage( body, message) {
	var jsonStart = body.indexOf( '"{') + 1;
	if ( jsonStart > -1) {
		var jsonEnd = body.indexOf('}"');
		var jsonString = body.substr( jsonStart, jsonEnd-jsonStart+1).toLowerCase();
		jsonString = jsonString.replace(/{/g,'{"'); // put quote at beginning of first field name
		jsonString = jsonString.replace(/:/g,'":'); // put ending quote around field names
		jsonString = jsonString.replace(/,/g,',"'); // put beginning quote around field names
		jsonString = jsonString.replace(/'/g,'"'); // replace single quotes with double quotes
		let j = JSON.parse( jsonString);
		j.msg = message;
		return j;
	}
}