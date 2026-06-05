async function submitMessage() {

    const name =
        document.getElementById("name").value;

    const message =
        document.getElementById("message").value;

    const response = await fetch(
        "https://vp0h5l3r3b.execute-api.eu-north-1.amazonaws.com/prod/messages",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name,
                message
            })
        }
    );

    const data = await response.json();

    document.getElementById("result").innerText =
        data.message;
}