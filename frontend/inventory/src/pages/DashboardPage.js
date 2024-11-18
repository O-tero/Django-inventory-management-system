import React from "react";
import Chart from "../components/Chart";
import Table from "../components/Table";
import Notification from "../components/Notification";

const DashboardPage = () => {
  return (
    <div className="dashboard-page">
      <h1>Dashboard</h1>
      <Notification message="Stock levels are running low for some items." />
      <div className="dashboard-content">
        <Chart title="Sales Overview" />
        <Chart title="Stock Levels" />
      </div>
      <Table
        title="Recent Orders"
        data={[
          { id: 1, item: "Brake Pads", status: "Shipped", quantity: 10 },
          { id: 2, item: "Engine Oil", status: "Pending", quantity: 20 },
        ]}
      />
    </div>
  );
};

export default DashboardPage;
