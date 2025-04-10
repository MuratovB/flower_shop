import React, { useState, useEffect } from 'react';

function ProfitLossReport() {
  const [reportData, setReportData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [period, setPeriod] = useState('2023-06');

  useEffect(() => {
    setLoading(true);
    setTimeout(() => {
      setReportData({
        period,
        revenue: 125000,
        expenses: 85000,
        profit: 40000,
        profitMargin: '32%'
      });
      setLoading(false);
    }, 1000);
  }, [period]);

  if (loading) return <div>Loading report...</div>;

  return (
    <div>
      <h3>Profit & Loss Report</h3>
      <div>
        <label>Select Period:</label>
        <input 
          type="month" 
          value={period}
          onChange={(e) => setPeriod(e.target.value)}
        />
      </div>
      <table>
        <tbody>
          <tr>
            <td>Period:</td>
            <td>{reportData.period}</td>
          </tr>
          <tr>
            <td>Revenue:</td>
            <td>${reportData.revenue.toLocaleString()}</td>
          </tr>
          <tr>
            <td>Expenses:</td>
            <td>${reportData.expenses.toLocaleString()}</td>
          </tr>
          <tr>
            <td>Profit:</td>
            <td>${reportData.profit.toLocaleString()}</td>
          </tr>
          <tr>
            <td>Profit Margin:</td>
            <td>{reportData.profitMargin}</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default ProfitLossReport;