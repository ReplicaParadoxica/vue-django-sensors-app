import Vue from 'vue'
import VueRouter from 'vue-router'
import Table from './views/Table'
import SensorDetail from './views/SensorDetail'
import MetricsList from './views/MetricsList'
import UnitsList from './views/UnitsList'
import MeasurementsList from './views/MeasurementsList'
Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/api/table',
            name: 'Table',
            component: Table
        },
        {
            path: '/api/sensors/:id/',
            name: 'SensorDetail',
            component: SensorDetail
        },
        {
            path: '/api/metrics/',
            name: 'MetricsList',
            component: MetricsList
        },
        {
            path: '/api/units/',
            name: 'UnitsList',
            component: UnitsList
        },
        {
            path: '/api/measurements/',
            name: 'MeasurementsList',
            component: MeasurementsList
        },
    ]
})
