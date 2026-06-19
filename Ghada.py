import turtle

# إنشاء النافذة وإعدادها
screen = turtle.Screen()
screen.title("عيد أضحى مبارك - من مبرمج")
screen.bgcolor("black")  # خلفية سوداء

# إنشاء السلحفاة للرسم والكتابة
t = turtle.Turtle()
t.hideturtle()
t.speed(3)

# 1. كتابة "Eid-Adha Mubarak" باللون الأصفر
t.penup()
t.goto(0, 150)  # الانتقال لأعلى قليلاً
t.color("yellow")
t.write("Eid-Adha Mubarak", align="center", font=("Arial", 28, "bold"))

# 2. رسم "خروف" بسيط (جسم أبيض)
t.goto(0, 0)
t.penup()
t.color("white")
t.begin_fill()
t.circle(60)  # جسم دائري أبيض
t.end_fill()

# إضافة تفاصيل بسيطة للوجه (عينين)
t.goto(-15, 60)
t.color("black")
t.begin_fill()
t.circle(5)  # عين يسرى
t.end_fill()
t.penup()
t.goto(15, 60)
t.begin_fill()
t.circle(5)  # عين يمنى
t.end_fill()

# 3. كتابة العبارة السفلية (POV)
t.goto(0, -150)
t.color("white")
t.write("POV: Eid-Adha Mubarak from a programmer", align="center", font=("Arial", 16, "normal"))

# إبقاء النافذة مفتوحة حتى الضغط عليها
screen.exitonclick()