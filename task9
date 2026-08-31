
APP_CONFIG = (
    ("APP_NAME", "Enterprise App"),
    ("VERSION", "1.0.0"),
    ("ENVIRONMENTS", ("Development", "Staging", "Production")),
    ("DATABASE_URL", "localhost:5432/mydb")
)

print("App Name:", APP_CONFIG[0][1])
print("Version:", APP_CONFIG[1][1])
print("Supported Environments:", APP_CONFIG[2][1])


print("\n--- Attempting Modification ---")
try:
    APP_CONFIG[0] = ("APP_NAME", "Hacked App")
except TypeError as e:
    print("Modification Failed! Error:", e)
