<template>
    <div>
        <h2>Measurements</h2>
        <div class="search-container">
            <input v-model="searchText" type="text" placeholder="Search by metric name">
        </div>
        <div class="measurement-checkboxes">
            <label>
                <input type="checkbox" v-model="showSensorName"> Sensor Name
            </label>
            <label>
                <input type="checkbox" v-model="showMetricName"> Metric Name
            </label>
            <label>
                <input type="checkbox" v-model="showUnitName"> Unit Name
            </label>
            <label>
                <input type="checkbox" v-model="showUnitPrecision"> Unit Precision
            </label>
            <label>
                <input type="checkbox" v-model="showValue"> Value
            </label>
        </div>
        <table>
            <thead>
                <tr>
                    <th v-if="showSensorName" @click="sort('sensor_name')">Sensor Name</th>
                    <th v-if="showMetricName" @click="sort('metric_name')">Metric Name</th>
                    <th v-if="showUnitName" @click="sort('unit_name')">Unit Name</th>
                    <th v-if="showUnitPrecision" @click="sort('unit_precision')">Unit Precision</th>
                    <th v-if="showValue" @click="sort('value')">Value</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(measurement, index) in filteredMeasurements" :key="index">
                    <td v-if="showSensorName">{{ measurement.sensor_name }}</td>
                    <td v-if="showMetricName">{{ measurement.metric_name }}</td>
                    <td v-if="showUnitName">{{ measurement.unit_name }}</td>
                    <td v-if="showUnitPrecision">{{ measurement.unit_precision }}</td>
                    <td v-if="showValue">{{ measurement.value }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    name: 'MeasurementList',
    data() {
        return {
            measurements: [],
            sortBy: null,
            sortDesc: false,
            searchText: '',
            showSensorName: true,
            showMetricName: true,
            showUnitName: true,
            showUnitPrecision: true,
            showValue: true,
        };
    },
    methods: {
        loadMeasurements() {
            axios
                .get('http://127.0.0.1:8000/api/measurements/')
                .then((response) => {
                    this.measurements = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        sort(column) {
            if (this.sortBy === column) {
                this.sortDesc = !this.sortDesc;
            } else {
                this.sortBy = column;
                this.sortDesc = false;
            }

            this.measurements.sort((a, b) => {
                let aValue = a[this.sortBy];
                let bValue = b[this.sortBy];

                if (typeof aValue === 'string' && typeof bValue === 'string') {
                    aValue = aValue.toLowerCase();
                    bValue = bValue.toLowerCase();
                }

                if (aValue === bValue) {
                    return 0;
                } if (this.sortDesc) {
                    return aValue > bValue ? -1 : 1;
                } else {
                    return aValue < bValue ? -1 : 1;
                }
            });
        },
    },
    computed: {
        filteredMeasurements() {
            return this.measurements.filter((measurement) => {
                const searchTextLower = this.searchText.toLowerCase();
                return (
                    measurement.sensor_name.toLowerCase().includes(searchTextLower) ||
                    measurement.metric_name.toLowerCase().includes(searchTextLower) ||
                    measurement.unit_name.toLowerCase().includes(searchTextLower)
                );
            });
        },
    },
    mounted() {
        this.loadMeasurements();
    },
};
</script>

<style scoped>
/* Add your styles here */

h2 {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 16px;
}

.search-container {
    margin-bottom: 16px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th,
td {
    padding: 8px;
    text-align: left;
    border: 1px solid #ccc;
}

tr:nth-child(even) {
    background-color: #f9f9f9;
}

tr:hover {
    background-color: #f2f2f2;
}

input[type="text"] {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 13px;
    width: 10%;
    box-sizing: border-box;
}

.metric-checkboxes {
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-bottom: 16px;
}

.metric-checkboxes label {
    margin-right: 16px;
}

.metric-checkboxes input[type="checkbox"] {
    margin-right: 8px;
}
</style>
  