export const decodeModel = (model) => {
	model.created = (new Date(model.created)).toLocaleDateString()

	const metrics = [];
	for (const key in model.metrics) {
		metrics.push({
			id: key,
			value: model.metrics[key]
		})
	}
	model.metrics = metrics;

	const parameters = [];
	for (const key in model.parameters) {
		parameters.push({
			id: key,
			value: model.parameters[key]
		})
	}
	model.parameters = parameters;

	const hyperparameters = [];
	for (const key in model.hyperparameters) {
		hyperparameters.push({
			id: key,
			value: model.hyperparameters[key]
		})
	}
	model.hyperparameters = hyperparameters;
	
	return model;
}