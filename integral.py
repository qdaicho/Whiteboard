def func1(n):
  return "∫X^" + str(n) + "dx\n" + "\nStep 1) Applying power rule:\n" + "x^" + str(n) + "+ 1 / " + str(n) + "+ 1\n" + "X^" + str(n + 1) + "/" + str(n + 1) + "+C" + "\n"


def func2(n):
  return "∫ 1/" + str(n) + "x dx \n"+"\nStep 1) Applying linearity:\n"+"\n1 / " + str(n) + " ∫1 / x dx\n"+"\nStep 2) Solving standard integral 1/x\n"+"\nAnswer:\n"+"ln |x|" + "/" + str(n) + " + C" + "\n"


def func3(n):
  text = "∫e^" + str(n) + "x dx\n"
  if(n == 1):
    text += "\nStep 1) Applying exponential rule a = e\n"
    text += "\ne^x / ln (e)\n"
    text += "\nln and e cancel each other leaving us with 1 in the denominator\n"
    text += "\nAnswer:\n"
    text += "e^x + C\n"
  else:
    text += "\nStep 1) Substitution rule:\n"
    text += "\nu = " + str(n) + "x and dx = 1 / " + str(n) + "du\n"
    text += "\nStep 2) Apply exponential rule:\n"
    text += "\n e^u / ln (e) \n"
    text += "\nln and e cancel each other leaving us with 1 in the denominator\n"
    text += "Step 3) Undo substitution\n"
    text += "\nAnswer:\n"
    text += "(e^" + str(n) + "x)" + "/" + str(n) + "\n"

  return text


def func4(a, b):
  text = "\n" + "∫" + str(a) + "^" + str(b) + "x dx" + "\n"
  if(b == 1):
    text += "Step 1) Applying exponential rule:\n"
    text += str(a) + "^x" + "/ " + "ln (" + str(a) + ")"
    text += "Answer:"
    text += "\n" + str(a) + "^x" + "/" + "ln" + str(a) + "+ C\n"
  else:
    text +=  "\nStep 1) Substitution rule:\n"
    text +=  "\nu = " + str(b) + "x and dx = 1 / " + str(b) + "\n"
    text +=  "\nStep 2) Applying exponential rule:\n"
    text +=  str(a) + "^u / ln(" + str(a) + ")\n"
    text +=  "\nStep 3) Undo substitution:\n"
    text +=  "\nAnswer:\n"
    text +=  "\n(" + str(a) + "^" + str(b) + "x" + ")/(" + str(b) + " * ln" + str(a) + ") + C" + "\n"

  return text

def func5(n):
  text = "\n" + "∫sin" + str(n) + "x dx" + "\n"
  if(n == 1):
    text += "\nStep 1) Standard integral form\n"
    text += "\nAnswer:\n"
    text += "\n" + "-cos x + C\n"
  else:
    text += "\nStep 1) Substitution rule:\n"
    text += "\nu = " + str(n) + "x and dx = 1 / " + str(n) + "\n"
    text += "\nStep 2) Solving standard form ∫ sin(u) du\n"
    text += "\nStep 3) Undo substitution\n"
    text += "\nAnswer:\n"
    text += "\n" + "-(cos" + str(n) + "x)" + "/" + str(n) + "+ C\n"

  return text

def func6(n):
  text = "\n" + "∫cos" + str(n) + "x dx" + "\n"
  if(n == 1):
    text += "\nStep 1) Standard integral form\n"
    text += "\nAnswer:\n"
    text += "\n" + "sin x + C\n"
  else:
    text += "\nStep 1) Substitution rule:\n"
    text += "\nu = " + str(n) + "x and dx = 1 / " + str(n) + "\n"
    text += "\nStep 2) Solving standard form ∫ cos(u) du\n"
    text += "\nStep 3) Undo substitution\n"
    text += "\nAnswer:\n"
    text += "\n" + "(sin" + str(n) + "x)" + "/" + str(n) + "+ C\n"

  return text


def func7(n):
  text = "\n" + "∫tan" + str(n) + "x dx" + "\n"
  if(n == 1):
    text += "\nStep 1) Standard integral form\n"
    text += "\nAnswer:\n"
    text += "\n" + "ln(|sec x|) +C" + "\n"
  else:
    text += "\nStep 1) Substitution rule:\n"
    text += "\nu = " + str(n) + "x and dx = 1 / " + str(n) + "\n"
    text += "\nStep 2) Solving standard form ∫ tan(u) du\n"
    text += "\nStep 3) Undo substitution\n"
    text += "\nAnswer:\n"
    text += "\n" + "(ln|sec" + str(n) + "x|)" + "/" + str(n) + " + C" + "\n"

  return text


def func8(n):
  text = "∫ csc" + str(n) + "x dx" + "\n"
  if(n == 1):
    text += "\nStep 1) Standard integral form\n"
    text += "\nAnswer:\n"
    text += "\n" + "ln(|csc x - cot x|) +C" + "\n"
  else:
    text += "\nStep 1) Substitution rule:\n"
    text += "\nu = " + str(n) + "x and dx = 1 / " + str(n) + "\n"
    text += "\nStep 2) Solving standard form ∫ csc(u) du\n"
    text += "\nStep 3) Undo substitution\n"
    text += "\nAnswer:\n"
    text += "\n" + "(ln|csc" + str(n) + "x - cot" + str(n) + "x|)" + "/" + str(n) + " + C" + "\n"

  return text


def func9(n):
  text = "\n" + "∫sec" + str(n) + "x dx" + "\n"
  if(n == 1):
    text += "\nStep 1) Standard integral form\n"
    text += "\nAnswer:\n"
    text += "\nln|sec x + tan x| + C\n"
  else:
    text += "\nStep 1) Substitution rule:\n"
    text += "\nu = " + str(n) + "x and dx = 1 / " + str(n) + "\n"
    text += "\nStep 2) Solving standard form ∫ sec(u) du\n"
    text += "\nStep 3) Undo substitution\n"
    text += "\nAnswer:\n"
    text += "\nln(|sec" + str(n) + "x + tan" + str(n) + "x )/" + str(n) + " + C" + "\n"

  return text


def func10(n):
  text = "\n∫cot" + str(n) + "x dx" + "\n"
  if(n == 1):
    text += "\nStep 1) Standard integral form\n"
    text += "\nAnswer:\n"
    text += "\nln|sin x| + C\n"
  else:
    text += "\nStep 1) Substitution rule:\n"
    text += "\nu = " + str(n) + "x and dx = 1 / " + str(n) + "\n"
    text += "\nStep 2) Solving standard form ∫ cot(u) du\n"
    text += "\nStep 3) Undo substitution\n"
    text += "\nAnswer:\n"
    text += "\nln(|sin" + str(n) + "x|) /" + str(n) + " + C\n"

  return text


def func11(n):
  text = "\n∫sec^2(" + str(n) + "x) dx\n"
  if(n == 1):
    text += "\nStep 1) Standard integral form\n"
    text += "\nAnswer:\n"
    text += "\n tan x + C\n"
  else:
    text += "\nStep 1) Substitution rule:\n"
    text += "\nu = " + str(n) + "x and dx = 1 / " + str(n) + "\n"
    text += "\nStep 2) Solving standard form ∫ sec^2(u) du\n"
    text += "\nStep 3) Undo substitution\n"
    text += "\nAnswer:\n"
    text += "\n(tan" + str(n) + "x)/" + str(n) + " + C\n"

  return text


def func12(n):
  text = "\n∫csc^2(" + str(n) + "x) dx\n"
  if(n == 1):
    text += "\nStep 1) Standard integral form\n"
    text += "\nAnswer:\n"
    text += "\n-cot x + C\n"
  else:
    text += "\nStep 1) Substitution rule:\n"
    text += "\nu = " + str(n) + "x and dx = 1 / " + str(n) + "\n"
    text += "\nStep 2) Solving standard form ∫ csc^2(u) du\n"
    text += "\nStep 3) Undo substitution\n"
    text += "\nAnswer:\n"
    text += "\n-(cot" + str(n) + "x)/" + str(n) + " + C\n"

  return text


def func13(n):
  text = "\n∫sec" + str(n) + "x tan" + str(n) + "x dx\n"
  if(n == 1):
    text += "\nStep 1) Standard integral form\n"
    text += "\nAnswer:\n"
    text += "\nsec x + C\n"
  else:
    text += "\nStep 1) Substitution rule:\n"
    text += "\nu = " + str(n) + "x and dx = 1 / " + str(n) + "\n"
    text += "\nStep 2) Solving standard form ∫ sec(u) tan(u) du\n"
    text += "\nStep 3) Undo substitution\n"
    text += "\nAnswer:\n"
    text += "\n(sec" + str(n) + "x)/" + str(n) + " + C\n"

  return text


def func14(n):
  text = "\n∫csc" + str(n) + "x cot" + str(n) + "x dx\n"
  if(n == 1):
    text += "\nStep 1) Standard integral form\n"
    text += "\nAnswer:\n"
    text += "\n-csc x + C\n"
  else:
    text += "\nStep 1) Substitution rule:\n"
    text += "\nu = " + str(n) + "x and dx = 1 / " + str(n) + "\n"
    text += "\nStep 2) Solving standard form ∫ csc(u) cot(u) du\n"
    text += "\nStep 3) Undo substitution\n"
    text += "\nAnswer:\n"
    text += "\n-(csc" + str(n) + "x)/" + str(n) + " + C\n"

  return text

def func15(n):
  text = "\n∫1/(sqrt(1-(" + str(n) + "x)^2) dx\n"
  if(n == 1):
    text += "\nStep 1) Standard integral form\n"
    text += "\nAnswer:\n"
    text += "\narcsin(x) + C\n"
  else:
    text += "\nStep 1) Substitution rule:\n"
    text += "\nu = " + str(n) + "x and dx = 1 / " + str(n) + "\n"
    text += "\nStep 2) Solving standard form ∫ 1 / sqrt(1-u^2) du\n"
    text += "\nStep 3) Undo substitution\n"
    text += "\nAnswer:\n"
    text += "\narcsin(" + str(n) + "x)/" + str(n) + " + C\n"
  return text


def func16(n):
  text = "\n∫-1/(sqrt(1-(" + str(n) + "x)^2) dx\n"
  if(n == 1):
    text += "\nStep 1) Standard integral form\n"
    text += "\nAnswer:\n"
    text += "\narccos(x) + C\n"
  else:
    text += "\nStep 1) Substitution rule:\n"
    text += "\nu = " + str(n) + "x and dx = 1 / " + str(n) + "\n"
    text += "\nStep 2) Solving standard form ∫ -1 / sqrt(1-u^2) du\n"
    text += "\nStep 3) Undo substitution\n"
    text += "\nAnswer:\n"
    text += "\narccos(" + str(n) + "x)/" + str(n) + " + C\n"
  return text


def func17(n):
  text = "\n∫1/(1+(" + str(n) + "x)^2) dx\n"
  if(n == 1):
    text += "\nStep 1) Standard integral form\n"
    text += "\nAnswer:\n"
    text += "\narctan(x) + C\n"
  else:
    text += "\nStep 1) Substitution rule:\n"
    text += "\nu = " + str(n) + "x and dx = 1 / " + str(n) + "\n"
    text += "\nStep 2) Solving standard form ∫ 1 / (1 + u^2) du\n"
    text += "\nStep 3) Undo substitution\n"
    text += "\nAnswer:\n"
    text += "\narctan(" + str(n) + "x)/" + str(n) + " + C\n"
  return text


def func18(n):
  text = "\n∫sinh" + str(n) + "x dx\n"
  if(n == 1):
    text += "\nStep 1) Standard integral form\n"
    text += "\nAnswer:\n"
    text += "\ncosh x + C\n"
  else:
    text += "\nStep 1) Substitution rule:\n"
    text += "\nu = " + str(n) + "x and dx = 1 / " + str(n) + "\n"
    text += "\nStep 2) Solving standard form ∫ sinh (u) du\n"
    text += "\nStep 3) Undo substitution\n"
    text += "\nAnswer:\n"
    text += "\ncosh(" + str(n) + "x)/" + str(n) + " + C\n"
  return text


def func19(n):
  text = "\n∫cosh" + str(n) + "x dx\n"
  if(n == 1):
    text += "\nStep 1) Standard integral form\n"
    text += "\nAnswer:\n"
    text += "\nsinh x + C\n"
  else:
    text += "\nStep 1) Substitution rule:\n"
    text += "\nu = " + str(n) + "x and dx = 1 / " + str(n) + "\n"
    text += "\nStep 2) Solving standard form ∫ cosh (u) du\n"
    text += "\nStep 3) Undo substitution\n"
    text += "\nAnswer:\n"
    text += "\nsinh(" + str(n) + "x)/" + str(n) + " + C\n"
  return text


print(func19(30))