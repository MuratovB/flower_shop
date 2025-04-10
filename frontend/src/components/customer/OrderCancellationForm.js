import React, { useState } from 'react';

function OrderCancellationForm() {
  const [orderId, setOrderId] = useState('');
  const [reason, setReason] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Cancelling order:', { orderId, reason });
    setIsSubmitted(true);
  };

  if (isSubmitted) {
    return <div>Your order cancellation request has been submitted.</div>;
  }

  return (
    <div>
      <h3>Order Cancellation Form</h3>
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
        <div>
          <label>Reason for cancellation:</label>
          <textarea 
            value={reason}
            onChange={(e) => setReason(e.target.value)}
            required
          />
        </div>
        <button type="submit">Submit Cancellation</button>
      </form>
    </div>
  );
}

export default OrderCancellationForm;