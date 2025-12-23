import os
from pyecore.resources import ResourceSet, URI
from pyecore.ecore import EPackage, EClass, EAttribute, EString, EReference

# --- 1. 定义Ecore 文件路径 ---
# 使用 r"..." raw string 格式来处理 Windows 路径中的反斜杠 \
model_directory = r"D:\EclipseWorkspace\test\model"
ecore_file_name = 'library.ecore'
ecore_file_path = os.path.join(model_directory, ecore_file_name)

# 确保目标目录存在
print(f"--- 检查目录: {model_directory} ---")
os.makedirs(model_directory, exist_ok=True)
print("目录存在。")
print("-" * 40)

# --- 阶段 1: 在指定路径创建示例元模型 'library.ecore' ---

print(f"--- 阶段 1: 正在创建元模型 '{ecore_file_path}' ---")

# 1. 创建元模型定义
LibraryPackage = EPackage(name='library', nsURI='http://example.org/library', nsPrefix='lib')
Book = EClass('Book')
Author = EClass('Author')
Book.eStructuralFeatures.append(EAttribute('title', EString))
Author.eStructuralFeatures.append(EAttribute('name', EString))
books_ref = EReference('books', Book, upper=-1, containment=True)
Author.eStructuralFeatures.append(books_ref)
LibraryPackage.eClassifiers.extend([Book, Author])

# 2. 保存这个元模型到 .ecore 文件
rset_saver = ResourceSet()
#    使用我们指定的完整路径创建资源
resource_saver = rset_saver.create_resource(URI(ecore_file_path))
resource_saver.append(LibraryPackage)
resource_saver.save()

print(f"文件 '{ecore_file_path}' 已创建。")
print("-" * 40)

# --- 阶段 2: 从指定路径加载 'library.ecore' 元模型 ---

print(f"--- 阶段 2: 正在加载 '{ecore_file_path}' 元模型 ---")

# 1. 检查文件是否存在
if not os.path.exists(ecore_file_path):
    print(f"错误: 文件 '{ecore_file_path}' 未找到。")
else:
    # 2. 创建一个新的资源集 (ResourceSet)
    rset_loader = ResourceSet()

    # 3. 从资源集中获取资源 (即加载文件)
    #    使用我们指定的完整路径
    resource = rset_loader.get_resource(URI(ecore_file_path))

    # 4. 获取元模型的根包 (EPackage)
    metamodel_root = resource.contents[0]

    # 5. 验证加载是否成功
    print(f"成功加载元模型！")
    print(f"  包 (Package) 名称: {metamodel_root.name}")
    print(f"  包 (Package) URI: {metamodel_root.nsURI}")

    # 6. 遍历并打印元模型中的所有类及其属性
    print("\n  元模型中的类 (EClassifiers):")
    for eclassifier in metamodel_root.eClassifiers:
        if isinstance(eclassifier, EClass):
            print(f"    - 类 (EClass): {eclassifier.name}")
            # 打印这个类的所有属性和引用
            for feature in eclassifier.eStructuralFeatures:
                if isinstance(feature, EAttribute):
                    print(f"      - 属性 (EAttribute): {feature.name} (类型: {feature.eType.name})")
                elif isinstance(feature, EReference):
                    print(f"      - 关联 (EReference): {feature.name} (指向: {feature.eType.name})")