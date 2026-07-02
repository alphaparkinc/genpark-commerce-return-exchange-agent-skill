from typing import Dict, Any
from datetime import datetime

class ReturnExchangeClient:
    def evaluate_eligibility(self, purchase_date_str: str, current_date_str: str, reason: str) -> Dict[str, Any]:
        p_date = datetime.strptime(purchase_date_str, "%Y-%m-%d")
        c_date = datetime.strptime(current_date_str, "%Y-%m-%d")
        days = (c_date - p_date).days
        eligible = days <= 30
        fee = 0.0
        if eligible and "changed my mind" in reason.lower():
            fee = 9.99  # Restocking fee
        return {
            "eligible": eligible,
            "days_since_purchase": days,
            "restocking_fee": fee,
            "rma_number": f"RMA-{purchase_date_str.replace('-', '')}-ELIG" if eligible else "N/A"
        }
