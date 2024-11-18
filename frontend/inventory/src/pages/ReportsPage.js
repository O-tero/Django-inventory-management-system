import React from "react";
import Chart from "../components/Chart";

const ReportsPage = () => {
  return (
    <div className="reports-page">
      <h1>Reports</h1>
      <div className="reports-charts">
        <Chart title="Sales Performance" />
        <Chart title="Inventory Trends" />
        <Chart title="Supplier Statistics" />
      </div>
    </div>
  );
};

export default ReportsPage;
