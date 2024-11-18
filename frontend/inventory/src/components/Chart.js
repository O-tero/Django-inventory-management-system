import React from "react";
import { Line } from "react-chartjs-2";

const Chart = ({ data }) => {
  const chartData = {
    labels: data.map((item) => item.label),
    datasets: [
      {
        label: "Sales",
        data: data.map((item) => item.value),
        borderColor: "blue",
        backgroundColor: "lightblue",
        fill: true,
      },
    ],
  };

  return (
    <div className="chart-container">
      <Line data={chartData} />
    </div>
  );
};

export default Chart;
