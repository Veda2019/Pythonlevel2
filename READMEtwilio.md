# 🏦 Bank Transaction SMS Notifier

A Python-based banking simulation that sends **real-time SMS notifications** via [Twilio](https://www.twilio.com/) for every deposit and withdrawal, with full transaction logging.

---

## 📋 Features

- 💸 **Withdraw & Deposit** operations with balance validation
- 📲 **SMS Alerts** via Twilio for every transaction (success or failure)
- 📝 **Logging** of all events to `bank_transactions.log`
- ⚠️ **Custom Exception Handling** with `InvalidAccountError`

---

## 🛠️ Prerequisites

- Python 3.7+
- A [Twilio account](https://www.twilio.com/try-twilio) (free trial available)

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/bank-sms-notifier.git
   cd bank-sms-notifier
   ```

2. **Install dependencies**
   ```bash
   pip install twilio
   ```

---

## ⚙️ Configuration

Open `bank_account.py` and fill in your Twilio credentials inside the `BankAccount.__init__` method:

```python
self.account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'   # Your Twilio Account SID
self.auth_token  = 'your_auth_token_here'                 # Your Twilio Auth Token
self.twilio_number = '+1XXXXXXXXXX'                       # Your Twilio phone number
```

> 🔑 Find these in your [Twilio Console](https://console.twilio.com/).

---

## 🚀 Usage

Run the script:

```bash
python bank_account.py
```

You will be prompted to:
1. Enter a **withdrawal amount** (₹)
2. Enter a **deposit amount** (₹)

**Example session:**
```
Enter amount to withdraw (₹): 200
Withdrawal attempt completed.

Enter amount to deposit (₹): 500
Deposit attempt completed.
```

An SMS will be sent to the registered phone number after each operation.

---

## 📁 Project Structure

```
bank-sms-notifier/
│
├── bank_account.py          # Main application file
├── bank_transactions.log    # Auto-generated transaction log
└── README.md                # Project documentation
```

---

## 📄 Logging

All events are logged to `bank_transactions.log` with the following levels:

| Level      | Event                                      |
|------------|--------------------------------------------|
| `INFO`     | Account creation, successful transactions  |
| `WARNING`  | Failed transactions (e.g. insufficient funds) |
| `ERROR`    | SMS delivery failures                      |
| `CRITICAL` | Unexpected application errors              |

Twilio's own internal logs are suppressed below `WARNING` to keep logs clean.

---

## 🧩 Class Overview

### `BankAccount`
| Method | Description |
|--------|-------------|
| `__init__(account_number, balance, phone_number)` | Creates account and initializes Twilio client |
| `deposit(amount)` | Deposits amount; raises error if ≤ 0 |
| `withdraw(amount)` | Withdraws amount; raises error if insufficient funds |
| `send_sms(message)` | Sends SMS notification via Twilio |

### `InvalidAccountError`
Custom exception raised for invalid banking operations (negative deposits, overdrafts).

---

## ⚠️ Important Notes

- **Never hardcode credentials** in production. Use environment variables:
  ```python
  import os
  self.account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
  self.auth_token  = os.environ.get('TWILIO_AUTH_TOKEN')
  ```
- Twilio **free trial** accounts can only send SMS to verified phone numbers.
- The currency symbol used is **Indian Rupee (₹)**; adjust as needed.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
