//https://github.com/microsoft/vscode-cpptools/issues/7413#issuecomment-827172897
#if __INTELLISENSE__
#undef __ARM_NEON
#undef __ARM_NEON__
#endif
#pragma once

#include <string>
#include <iostream>
namespace dblidar {



  /**
   * @brief A class for saying hello in multiple languages
   */
  class ExampleClass {

  public:
    ExampleClass(){
      std::cout << "Default example class" << std::endl;
    }
    ExampleClass(std::string name){
      std::cout << "Example class with name: " << name << std::endl;
    }
    void print();
    
  };

}  // namespace dbslam
