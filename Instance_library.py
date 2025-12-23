import os
from pyecore.resources import ResourceSet, URI

# --- 1. 定义文件路径 ---
model_directory = r"D:\EclipseWorkspace\test\model"
ecore_file_name = 'library.ecore'
xmi_file_name = 'my_library_instance.xmi'  # 这是我们将要生成的实例化XML文件

ecore_file_path = os.path.join(model_directory, ecore_file_name)
xmi_file_path = os.path.join(model_directory, xmi_file_name)

# 确保目录存在
os.makedirs(model_directory, exist_ok=True)

# --- 2. 你的 Ecore 元模型内容 ---
# (这就是你提供的 XML 内容)
ecore_content = """<?xml version='1.0' encoding='UTF-8'?>
<ecore:EPackage xmlns:xmi="http://www.omg.org/XMI" xmlns:ecore="http://www.eclipse.org/emf/2002/Ecore" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="library" nsURI="http://example.org/library" nsPrefix="lib" xmi:version="2.0">
  <eClassifiers xsi:type="ecore:EClass" name="Book">
    <eStructuralFeatures xsi:type="ecore:EAttribute" name="title" eType="ecore:EDataType http://www.eclipse.org/emf/2002/Ecore#//EString"/>
  </eClassifiers>
  <eClassifiers xsi:type="ecore:EClass" name="Author">
    <eStructuralFeatures xsi:type="ecore:EAttribute" name="name" eType="ecore:EDataType http://www.eclipse.org/emf/2002/Ecore#//EString"/>
    <eStructuralFeatures xsi:type="ecore:ERefere
nce" name="books" eType="#//Book" upperBound="-1" containment="true"/>
  </eClassifiers>
</ecore:EPackage>
"""

# 将元模型内容写入文件
try:
    with open(ecore_file_path, 'w', encoding='utf-8') as f:
        # 修复你提供的 XML 中 EReference 标签在 'Refere' 处的换行符
        ecore_content = ecore_content.replace("ecore:ERefere\nnce", "ecore:EReference")
        f.write(ecore_content)
    print(f"--- 成功将元模型写入: {ecore_file_path} ---")
except IOError as e:
    print(f"写入 Ecore 文件时出错: {e}")
    exit()

# --- 3. 加载 Ecore 元模型并准备实例化 ---
print(f"--- 正在加载元模型: {ecore_file_path} ---")

rset = ResourceSet()
resource = rset.get_resource(URI(ecore_file_path))
metamodel_root = resource.contents[0]

# 注册元模型 (这是解决 Eclipse "PackageNotFound" 错误的关键步骤)
rset.metamodel_registry[metamodel_root.nsURI] = metamodel_root
print(f"元模型 {metamodel_root.name} (URI: {metamodel_root.nsURI}) 已加载并注册。")

# --- 4. 实例化模型 (创建对象) ---
print("\n--- 正在实例化模型... ---")

try:
    # 4.1 按名称获取类
    Author = metamodel_root.getEClassifier('Author')
    Book = metamodel_root.getEClassifier('Book')

    # 4.2 创建实例
    author_instance = Author()
    book1_instance = Book()
    book2_instance = Book()

    # 4.3 设置属性
    author_instance.name = "J. R. R. Tolkien"
    book1_instance.title = "The Hobbit"
    book2_instance.title = "The Lord of the Rings"

    print(f"已创建实例: {author_instance.name}")

    # 4.4 建立关联 (因为是 containment, 所以是 "包含" 关系)
    author_instance.books.append(book1_instance)
    author_instance.books.append(book2_instance)

    print(f"  - 已添加 Book: {book1_instance.title}")
    print(f"  - 已添加 Book: {book2_instance.title}")

except Exception as e:
    print(f"实例化时出错: {e}")
    exit()

# --- 5. 将实例模型保存为 XMI 文件 (即 "实例化的 XML") ---
print(f"\n--- 正在将实例保存到: {xmi_file_path} ---")

# 5.1 创建一个新的资源来保存 XMI
instance_resource = rset.create_resource(URI(xmi_file_path))

# 5.2 将根对象 (author_instance) 添加到资源中
#     PyEcore 会自动处理它所 "包含" 的所有子对象 (book1 和 book2)
instance_resource.append(author_instance)

# 5.3 保存文件
instance_resource.save()

print("--- 实例化完成！---")
print(f"XMI 实例文件已生成: {xmi_file_path}")