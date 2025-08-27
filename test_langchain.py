#!/usr/bin/env python3
"""
Basic LangChain example to verify installation and demonstrate usage.
"""

from langchain.schema import HumanMessage, SystemMessage
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


def test_langchain_installation():
    """Test that LangChain is properly installed and can be imported."""
    try:
        # Test basic imports
        from langchain import __version__
        print(f"✅ LangChain successfully installed! Version: {__version__}")
        
        # Test creating a simple prompt template
        prompt = PromptTemplate.from_template("Hello, my name is {name}")
        formatted_prompt = prompt.format(name="Tony")
        print(f"✅ Prompt template created: '{formatted_prompt}'")
        
        # Test message creation
        system_msg = SystemMessage(content="You are a helpful assistant.")
        human_msg = HumanMessage(content="Hello, LangChain!")
        print(f"✅ Messages created successfully")
        print(f"   System: {system_msg.content}")
        print(f"   Human: {human_msg.content}")
        
        # Test output parser
        parser = StrOutputParser()
        print(f"✅ Output parser created: {type(parser).__name__}")
        
        return True
        
    except ImportError as e:
        print(f"❌ LangChain import failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Error testing LangChain: {e}")
        return False


if __name__ == "__main__":
    print("🔍 Testing LangChain installation...")
    success = test_langchain_installation()
    
    if success:
        print("\n🎉 LangChain is ready to use!")
        print("\n📚 To get started with LangChain:")
        print("   1. Check out the documentation: https://python.langchain.com/")
        print("   2. Try building your first chain")
        print("   3. Explore different LLM integrations")
    else:
        print("\n❌ LangChain installation test failed!")
        exit(1)