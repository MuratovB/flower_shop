import React, { useState } from 'react';

function OrderEditForm() {
  const [orderId, setOrderId] = useState('');
  const [changes, setChanges] = useState({
    items: [],
    customerInfo: '',
    deliveryDate: '',
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Updating order:', { orderId, changes });
  };

  return (
    <div>
      <h3>Edit Order</h3>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Order ID:</label>
          <input 
            type="text" 
            value={orderId}
            onChange={(e) => setOrderId(e.target.value)}
            required
          />
        </div>
        <button type="submit">Save Changes</button>
      </form>
    </div>
  );
}

export default OrderEditForm;