import React, { useState, useEffect } from 'react';

function CustomerOrders() {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setTimeout(() => {
      setOrders([
        { id: 1, date: '2023-05-01', amount: 150.00, status: 'Completed' },
        { id: 2, date: '2023-05-15', amount: 89.99, status: 'Processing' },
        { id: 3, date: '2023-06-02', amount: 45.50, status: 'Shipped' }
      ]);
      setLoading(false);
    }, 1000);
  }, []);

  if (loading) return <div>Loading orders...</div>;

  return (
    <div>
      <h3>My Orders</h3>
      <table>
        <thead>
          <tr>
            <th>Order ID</th>
            <th>Date</th>
            <th>Amount</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {orders.map(order => (
            <tr key={order.id}>
              <td>{order.id}</td>
              <td>{order.date}</td>
              <td>${order.amount.toFixed(2)}</td>
              <td>{order.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default CustomerOrders;