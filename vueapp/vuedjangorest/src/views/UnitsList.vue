<template>
    <div>
        <h2>Units</h2>
        <div class="search-container">
            <input v-model="searchText" type="text" placeholder="Search by metrics name">
        </div>
        <div class="unit-checkboxes">
            <label>
                <input type="checkbox" v-model="showId"> ID
            </label>
            <label>
                <input type="checkbox" v-model="showName"> Name
            </label>
            <label>
                <input type="checkbox" v-model="showMetric"> Metrics name
            </label>
            <label>
                <input type="checkbox" v-model="showPrecision"> Precision
            </label>
        </div>
        <table>
            <thead>
                <tr>
                    <th v-if="showId" @click="sort('id')">ID</th>
                    <th v-if="showName" @click="sort('name')">Name</th>
                    <th v-if="showMetric" @click="sort('metric_name')">Metric</th>
                    <th v-if="showPrecision" @click="sort('precision')">Precision</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(unit, index) in filteredUnits" :key="index">
                    <td v-if="showId">{{ unit.id }}</td>
                    <td v-if="showName">{{ unit.name }}</td>
                    <td v-if="showMetric">{{ unit.metric_name }}</td>
                    <td v-if="showPrecision">{{ unit.precision }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>
import axios from 'axios';

export default {
    name: 'UnitList',
    data() {
        return {
            units: [],
            sortBy: null,
            sortDesc: false,
            searchText: '',
            showId: true,
            showName: true,
            showMetric: true,
            showPrecision: true,
        };
    },
    methods: {
        loadUnits() {
            axios
                .get('http://127.0.0.1:8000/api/units/')
                .then((response) => {
                    this.units = response.data;
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

            this.units.sort((a, b) => {
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
        filteredUnits() {
            const searchText = this.searchText.toLowerCase();
            return this.units.filter((unit) => {
                return unit.metric_name.toLowerCase().indexOf(searchText) !== -1;
            });
        },
    },
    mounted() {
        this.loadUnits();
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
  