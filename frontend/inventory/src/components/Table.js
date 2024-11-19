import React from "react";
import "../../styles/components/Table.css";

const Table = ({ columns, data, onRowClick, actions }) => {
  return (
    <div className="table-container">
      <table className="table">
        <thead>
          <tr>
            {columns.map((column, index) => (
              <th key={index}>{column.header}</th>
            ))}
            {actions && <th>Actions</th>}
          </tr>
        </thead>
        <tbody>
          {data.length > 0 ? (
            data.map((row, rowIndex) => (
              <tr
                key={rowIndex}
                onClick={() => onRowClick && onRowClick(row)}
                className={onRowClick ? "clickable-row" : ""}
              >
                {columns.map((column, colIndex) => (
                  <td key={colIndex}>{row[column.accessor]}</td>
                ))}
                {actions && (
                  <td className="action-buttons">
                    {actions.map((action, actionIndex) => (
                      <button
                        key={actionIndex}
                        className={action.className}
                        onClick={(e) => {
                          e.stopPropagation(); // Prevent triggering row click
                          action.onClick(row);
                        }}
                      >
                        {action.label}
                      </button>
                    ))}
                  </td>
                )}
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan={columns.length + (actions ? 1 : 0)} className="no-data">
                No data available
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default Table;
