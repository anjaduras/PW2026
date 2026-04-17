<script>
	import { onMount } from 'svelte';
	import Chart from 'chart.js/auto';

	let canvas;
	let chart;

	let labels = [];
	let dataPoints = [];

	onMount(() => {
		// small delay ensures DOM is ready
		setTimeout(() => {
			chart = new Chart(canvas, {
				type: 'line',
				data: {
					labels,
					datasets: [
						{
							label: 'Höhe (m)',
							data: dataPoints,
							borderWidth: 2,
							tension: 0.3
						}
					]
				},
				options: {
					responsive: true,
					maintainAspectRatio: false,
					animation: false
				}
			});

			setInterval(() => {
				const now = new Date().toLocaleTimeString();
				const height = 420 + Math.random() * 30;

				labels.push(now);
				dataPoints.push(height);

				if (labels.length > 20) {
					labels.shift();
					dataPoints.shift();
				}

				chart.update();
			}, 1000);
		}, 100);
	});
</script>

<h1>ESP Höhen Live Simulation</h1>

<div style="height: 400px;">
	<canvas bind:this={canvas}></canvas>
</div>