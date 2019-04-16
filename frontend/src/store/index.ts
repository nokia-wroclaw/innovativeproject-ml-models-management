import { any } from "prop-types";

type StoreHandler = (payload:any)=>void;
type Mutagen = (...args:any[])=>any;

class Data extends Map<string,DataPoint>{
	const ensure = (datapointId:string)=>{
		if(!data.has(datapointId)) data.set(datapointId,new DataPoint())
		return data.get(datapointId) as DataPoint;
	}
}
class DataPoint{
	subscribers = new Map<string,StoreHandler>();
	notify(){
		this.subscribers.forEach( sub => sub(this.payload) )
	}
	constructor(){}
}
class Mutation{
	datapoints:string[] = [""];
	mutagen:Mutagen;
	constructor(datapoints:string[],mutagen:Mutagen){
		this.datapoints = datapoints;
		this.mutagen = mutagen;
	}
	mutate=(...args:any[])=>{
		this.mutagen();
		this.datapoints.forEach( dp => data.ensure(dp).notify() )
	}
}

const data = new Data();

export const subscribe = (datapointId:string,subscriberId:string,onChange:StoreHandler) => {
	data.ensure(datapointId).subscribers.set(subscriberId,onChange);
}
export const unsubscribe = (datapointId:string,subscriberId:string) => {
	data.ensure(datapointId).subscribers.delete(subscriberId);
}


