from monitor import SystemMonitor
from remediation import AutoFixer
from predictor import Predictor
from notifier import Notifier

monitor = SystemMonitor()
fixer = AutoFixer()
predictor = Predictor()
notifier = Notifier()

def run_bot():
    issues = monitor.check_system()
    decision = predictor.analyze(issues)

    if decision.get("fix"):
        fixer.apply(decision["fix"])
    else:
        notifier.send_alert(issues)

if __name__ == "__main__":
    run_bot()
