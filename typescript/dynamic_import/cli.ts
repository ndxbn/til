import * as glob from "glob";

async function load() {
    for (const path of glob.sync("./lib/**/*.ts")) {
        console.log(path);
        const module = await import(path);
        console.log(module);
    };
}


load().then(() => {
    console.log("done.");
    process.exit();
});