import React from 'react';
import Chart from '../components/Chart';
import Notification from '../components/Notification';

const DashboardPage = () => (
    <div className="dashboard">
        <h1>Dashboard</h1>
        <div className="dashboard-metrics">
            <Notification message="Low Stock Alert: Part XYZ running low." />
            <div className="metric-card">Total Inventory: 1500 items</div>
            <div className="metric-card">Pending Orders: 35</div>
        </div>
        <Chart data={[ /* sales data here */ ]} />
    </div>
);

export default DashboardPage;
