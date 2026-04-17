<script>
    import { onMount, tick } from "svelte";
    import Chart from "chart.js/auto";

    let canvas;
    let chart;

    async function load() {
        const res = await fetch("/api/data");
        const data = await res.json();

        console.log("NEW DATA:", data[data.length - 1]);

        if (!chart) return;

        const labels = data.map((d) =>
            new Date(d.timestamp).toLocaleTimeString(),
        );

        const values = data.map((d) => d.altitude);

        chart.data.labels = labels;
        chart.data.datasets[0].data = values;

        chart.update("none"); // IMPORTANT: smoother + faster update
    }
    
    onMount(async () => {
        await tick();

        const ctx = canvas.getContext("2d");

        chart = new Chart(ctx, {
            type: "line",
            data: {
                labels: [],
                datasets: [
                    {
                        label: "Höhe",
                        data: [],
                        borderWidth: 2,
                    },
                ],
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                animation: {
                    duration: 300,
                },
            },
        });

        load();
        setInterval(load, 1000);
    });
</script>

<h1>Live Höhen Daten</h1>

<div style="height: 400px; width: 100%;">
    <canvas bind:this={canvas}></canvas>
</div>
