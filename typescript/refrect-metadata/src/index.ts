import "reflect-metadata";

function injectable() {
	return (classConstructor: Object) => {
		const metadataKeys = Reflect.getMetadataKeys(classConstructor);
		console.log(metadataKeys);
		for(const key of metadataKeys) {
			const metadata = Reflect.getMetadata(key, classConstructor);
			console.log(metadata);
		}
	};
}

@injectable()
class Demo {
	public readonly name: string;
	public readonly mail: string | undefined;
	public readonly nickname: string | undefined;

	// [ 'design:paramtypes' ]
	// [ [Function: String], [Function: Object], [Function: String] ]
	public constructor(name: string, mail: string | undefined, nickname?: string) {
		this.name = name;
		this.mail = mail;
		this.nickname = nickname;
	}
}

const instance = new Demo("my demo", undefined);
console.log(instance);
