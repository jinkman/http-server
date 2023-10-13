#include <iostream>
#include "httplib.h"

using namespace httplib;
int main(int argc, char **argv) {
    Server svr;
    svr.set_logger([](const Request &req, const Response &res) { std::cout << "hello world!" << std::endl; });

    svr.Get("/hi", [](const Request &req, Response &res) {
        std::cout << "hi" << std::endl;
        res.set_content("Hello World!", "text/plain");
    });

    svr.Get("/stop", [&](const Request &req, Response &res) {
        std::cout << "stop" << std::endl;
        svr.stop();
    });

    svr.listen("127.0.0.1", 8080);
    return 0;
}