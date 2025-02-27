const URL =  'http://127.0.0.1:5000';

    async function chamarApi() {
        const resp = await fetch(URL)
        if (resp.status === 200) {
            const obj = await resp.json();
            console.log(obj);
        }
}


chamarApi();