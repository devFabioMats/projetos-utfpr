const OrderServiceWithoutDIP = require('./project-without-dip/order-service');

const OrderServiceWithDIP = require('./project-with-dip/order-service');
const ConsoleLog = require('./project-with-dip/adapters/console-log');

function runProjectWithoutDIP() {
	console.log('Projeto sem DIP');

	const service = new OrderServiceWithoutDIP();
	service.finalizeOrder('Ana', 149.9);

	console.log('');
}

function runProjectWithDIP() {
	console.log('Projeto com DIP');

	const logConsole = new ConsoleLog();
	const serviceWithConsole = new OrderServiceWithDIP(logConsole);
	serviceWithConsole.finalizeOrder('Bruno', 299.5);
	console.log('');
}

function main() {
	runProjectWithoutDIP();
	runProjectWithDIP();
}

main();