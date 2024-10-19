import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

job_titles = {
    "مدیر بازاریابی": "Marketing Manager",
    "تحلیلگر داده": "Data Analyst",
    "برنامه‌نویس": "Programmer",
    "مدیر پروژه": "Project Manager",
    "طراح وب": "Web Designer",
    "تحلیلگر مالی": "Financial Analyst",
    "متخصص فناوری اطلاعات": "IT Specialist",
    "حسابدار": "Accountant",
    "مدیر منابع انسانی": "HR Manager",
    "مشاور کسب‌وکار": "Business Consultant",
    "مدیر فروش": "Sales Manager",
    "متخصص SEO": "SEO Specialist",
    "مدیر تولید": "Production Manager",
    "مهندس نرم‌افزار": "Software Engineer",
    "تحلیلگر سیستم": "Systems Analyst",
    "متخصص شبکه": "Network Specialist",
    "کارشناس حقوقی": "Legal Expert",
    "مدیر اجرایی": "Executive Director",
    "مدیر مالی": "Finance Manager",
    "مدیر ارتباط با مشتری": "Customer Relations Manager",
    "متخصص بازاریابی": "Marketing Specialist",
    "مدیر تحقیق و توسعه": "R&D Manager",
    "مشاور فناوری": "Technology Consultant",
    "مدیر IT": "IT Manager",
    "متخصص UX/UI": "UX/UI Specialist",
    "مدیر عملیات": "Operations Manager",
    "تحلیلگر بازار": "Market Analyst",
    "متخصص فروش": "Sales Specialist",
    "مدیر پروژه‌های فناوری": "Tech Project Manager",
    "مشاور مالی": "Financial Advisor",
    "مدیر استراتژی": "Strategy Manager",
    "متخصص امنیت سایبری": "Cybersecurity Specialist",
    "تحلیلگر کیفیت": "Quality Analyst",
    "مدیر تامین": "Supply Manager",
    "مدیر ارتباطات": "Communications Manager",
    "مدیر اجرایی فروش": "Sales Executive",
    "مدیر دیجیتال مارکتینگ": "Digital Marketing Manager",
    "تحلیلگر ریسک": "Risk Analyst",
    "متخصص داده": "Data Specialist",
    "مدیر کیفیت": "Quality Manager",
    "تحلیلگر شغلی": "Career Analyst",
    "مشاور بازاریابی دیجیتال": "Digital Marketing Consultant",
    "مدیر منابع مالی": "Financial Resources Manager",
    "تحلیلگر محصول": "Product Analyst",
    "مدیر ارتباطات بازار": "Market Communications Manager",
    "مدیر پروژه‌های بین‌المللی": "International Project Manager",
    "مشاور مدیریت پروژه": "Project Management Consultant",
    "مدیر فروش B2B": "B2B Sales Manager",
    "مدیر فروش B2C": "B2C Sales Manager",
    "مدیر استراتژی بازاریابی": "Marketing Strategy Manager",
    "تحلیلگر قیمت‌گذاری": "Pricing Analyst",
    "مدیر خدمات مشتری": "Customer Service Manager",
    "تحلیلگر تحقیق و توسعه": "R&D Analyst",
    "مشاور بهبود عملکرد": "Performance Improvement Consultant",
    "مدیر گردشگری": "Tourism Manager",
    "تحلیلگر بازار کار": "Labor Market Analyst",
    "مدیر ریسک": "Risk Manager",
    "تحلیلگر اقتصادی": "Economic Analyst",
    "مدیر فروش فیزیکی": "Physical Sales Manager",
    "مدیر توسعه محصول": "Product Development Manager",
    "تحلیلگر اطلاعات": "Information Analyst",
    "مشاور مدیریت مالی": "Financial Management Consultant",
    "مدیر پروژه‌های نوآورانه": "Innovative Project Manager",
    "تحلیلگر نوآوری": "Innovation Analyst",
    "مدیر تدارکات": "Procurement Manager",
    "تحلیلگر فعالیت": "Activity Analyst",
    "مدیر روابط عمومی": "Public Relations Manager",
    "تحلیلگر اجتماعی": "Social Analyst",
    "مدیر موفقیت مشتری": "Customer Success Manager",
    "تحلیلگر جغرافیایی": "Geographic Analyst",
    "مدیر پروژه‌های تحقیقاتی": "Research Project Manager",
    "تحلیلگر تجربیات کاربری": "User Experience Analyst"
}

def upload_file():
    """Upload a resume file."""
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                resume_text = file.read()
                recommendations = analyze_resume(resume_text)
                show_results(recommendations)
        except Exception as e:
            messagebox.showerror("خطا", f"مشکلی در خواندن فایل پیش آمد: {e}")

def analyze_resume(resume):
    """Analyze the resume text and provide job recommendations based on keywords."""
    recommendations = []

    keywords = {
        "برنامه‌نویس": ["برنامه‌نویس", "توسعه‌دهنده", "Python", "Java", "C++", "کدنویسی"],
        "حسابدار": ["حسابداری", "مالی", "گزارش مالی", "صورتحساب", "تحلیل مالی"],
        "مدیر فروش": ["فروش", "بازاریابی", "مدیریت فروش", "استراتژی فروش", "مشتری"],
        "تحلیلگر داده": ["تحلیل داده", "تحلیلگر", "آمار", "داده‌کاوی", "پایتون"],
        "مدیر پروژه": ["مدیریت پروژه", "برنامه‌ریزی", "تحلیل نیاز", "مدیریت منابع", "سازماندهی"],
        "طراح وب": ["طراحی وب", "HTML", "CSS", "JavaScript", "طراحی UI/UX"],
        "مدیر منابع انسانی": ["منابع انسانی", "استخدام", "مدیریت پرسنل", "رشد و توسعه", "آموزش"],
    }

    for job_title, words in keywords.items():
        if any(word in resume for word in words):
            recommendations.append(job_title)

    return recommendations or ["شغل مناسب پیدا نشد / No suitable job found"]

def show_results(recommendations):
    """Show the job recommendations and interview resources in a single window."""
    resources = [
        "1. https://www.glassdoor.com/Interview/index.htm",
        "2. https://www.thebalancecareers.com/interview-questions-2060797",
        "3. https://www.forbes.com/sites/allbusiness/2020/01/01/50-interview-questions-you-should-be-prepared-to-answer/",
        "4. https://www.indeed.com/career-advice/interviewing/interview-questions-and-answers",
        "5. https://www.themuse.com/advice/interview-preparation-guide"
    ]
    
    results_text = "پیشنهاد شغل:\n" + "\n".join(recommendations) + "\n\nمنابع آمادگی مصاحبه:\n" + "\n".join(resources)

    result_window = tk.Toplevel(root)
    result_window.title("نتایج")
    result_window.geometry("500x400")
    result_window.configure(bg="#f7f9fc")
    
    text_area = scrolledtext.ScrolledText(result_window, wrap=tk.WORD, bg="white", fg="#34495e", font=("Arial", 12))
    text_area.insert(tk.END, results_text)
    text_area.config(state=tk.DISABLED)
    text_area.pack(expand=True, fill='both', padx=10, pady=10)

# GUI setup
root = tk.Tk()
root.title("تحلیل رزومه")

# تنظیم اندازه پنجره
root.geometry("400x300")
root.configure(bg="#f7f9fc")

# طراحی پنجره
header_frame = tk.Frame(root, bg="#3498db")
header_frame.pack(fill=tk.X)

title_label = tk.Label(header_frame, text="پیشنهاد شغل بر اساس رزومه", font=("Arial", 16, "bold"), bg="#3498db", fg="white")
title_label.pack(pady=10)

upload_button = tk.Button(root, text="فایل رزومه را بارگذاری کنید", command=upload_file,
                          bg="#2ecc71", fg="white", font=("Arial", 12), padx=10, pady=5)
upload_button.pack(pady=20)

info_label = tk.Label(root, text="لطفا فایل رزومه خود را انتخاب کنید.", font=("Arial", 10), bg="#f7f9fc", fg="#34495e")
info_label.pack(pady=10)

root.mainloop()
