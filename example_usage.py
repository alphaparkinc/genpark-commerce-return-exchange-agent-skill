from client import ReturnExchangeClient
def main():
    c = ReturnExchangeClient()
    print(c.evaluate_eligibility("2026-06-15", "2026-07-02", "changed my mind"))
if __name__ == '__main__':
    main()
