"use strict"

const GetData = async () => {

    const response = await fetch("https://jsonplaceholder.typicode.com/users", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    });

    const data = response.json();
    return data;
};

const CreateElements = async (container, data) => {

    const
};

