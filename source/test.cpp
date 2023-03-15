#include <dblidar/types.h>
#include <iostream>
#include <Eigen/Dense>
#include <open3d/Open3D.h>
#include <spdlog/spdlog.h>
// using namespace dblidar;
void dblidar::ExampleClass::print() {
    // std::cout << "Hello World!" << std::endl;
    spdlog::info("Hello World!");
    spdlog::warn("Hello World!");
    spdlog::error("Hello World!");
    spdlog::critical("Hello World!");
    spdlog::debug("Hello World!");
    spdlog::set_level(spdlog::level::debug); 
    Eigen::MatrixXd m(2,2);
    m(0,0) = 3;
    m(1,0) = 2.5;
    m(0,1) = -1;
    m(1,1) = m(1,0) + m(0,1);
    std::cout << m << std::endl;
    using namespace open3d;
    utility::SetVerbosityLevel(utility::VerbosityLevel::Debug);
}