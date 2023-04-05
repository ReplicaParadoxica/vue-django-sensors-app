<template>
    <div class="container">
        <h2> Sensor Detail </h2>
        <table>
            <tr>
                <td>Name:</td>
                <td>{{ sensor.name }}</td>
            </tr>
            <tr>
                <td>Metrics:</td>
                <td>{{ formattedMetrics }}</td>
            </tr>
        </table>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    name: 'SensorDetail',
    data() {
        return {
            sensor: {},
        };
    },
    methods: {
        getSensorDetails() {
            const id = this.$route.params.id;
            axios.get(`http://localhost:8000/api/sensors/${id}/`).then((response) => {
                this.sensor = response.data;
            });
        },
    },
    computed: {
        formattedMetrics() {
            const metrics = this.sensor.metrics;
            if (metrics) {
                const metricKeys = Object.keys(metrics);
                const formattedMetrics = metricKeys.map((key) => {
                    const unit = metrics[key].unit;
                    const value = metrics[key].values[0].value;
                    return `${key}: ${value} ${unit}`;
                });
                return formattedMetrics.join(", ");
            }
            return "";
        },
    },
    created() {
        this.getSensorDetails();
    },
};
</script>
  
<style scoped>
table,
th,
td {
    border: 1px solid black;
    border-collapse: collapse;
}

th,
td {
    padding: 5px;
}

.container {
    margin: 20px;
}
</style>
