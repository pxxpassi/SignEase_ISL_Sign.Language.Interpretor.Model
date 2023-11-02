import 'package:flutter/material.dart';

class MyHome extends StatefulWidget {
  const MyHome({Key? key}) : super(key: key);

  @override
  _MyHomeState createState() => _MyHomeState();
}

class _MyHomeState extends State<MyHome> {
  void _navigateToHomePage() {
    // Add your navigation logic here, for example:
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) {// Replace this with the widget for the next page
          return const HomePage();
        },
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: const BoxDecoration(
        image: DecorationImage(
          image: AssetImage('assets/login.png'),
          fit: BoxFit.cover,
        ),
      ),
      child: Scaffold(
        backgroundColor: Colors.transparent,
        body: Stack(
          children: [
            Column(
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Container(
                  margin: const EdgeInsets.only(left: 90, right: 40, top: 30),
                  child: const Column(
                    children: [
                      SizedBox(
                        height: 550,
                      ),
                      Text(
                        'SIGNEASE',
                        style: TextStyle(
                          color: Color(0xFFE8BBB8),
                          fontSize: 50,
                          fontWeight: FontWeight.w900,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
            Container(
              margin: const EdgeInsets.only(left: 35, right: 35),
              padding: const EdgeInsets.only(left: 45, top: 650),
              child: const Text(
                'welcome back!',
                style: TextStyle(
                  color: Color(0xFFE8BBB8),
                  fontSize: 40,
                  fontWeight: FontWeight.w900,
                ),
              ),
            ),
            SingleChildScrollView(
              child: Container(
                padding: EdgeInsets.only(
                  top: MediaQuery.of(context).size.height * 0.5,
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Container(
                      margin: const EdgeInsets.only(left: 45, right: 35),
                      child: Column(
                        children: [
                          const SizedBox(
                            height: 300,
                          ),
                          Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              const Text(
                                'Get Started',
                                style: TextStyle(
                                  color: Color(0xFFE28F59),
                                  fontSize: 35,
                                  fontWeight: FontWeight.w400,
                                ),
                              ),
                              CircleAvatar(
                                radius: 30,
                                backgroundColor: const Color(0xFFE28F59),
                                child: IconButton(
                                  color: const Color(0xFF4D1B47),
                                  onPressed: _navigateToHomePage,
                                  icon: const Icon(
                                    Icons.arrow_forward,
                                  ),
                                ),
                              ),
                            ],
                          ),
                          const SizedBox(
                            height: 50,
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  _HomePageState createState() => _HomePageState();

}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: const BoxDecoration(
        image: DecorationImage(
          image: AssetImage('assets/login.png'),
          fit: BoxFit.cover,
        ),
      ),
      child: Scaffold(
          backgroundColor: Colors.transparent,
          appBar: AppBar(
            title: const Text('SignEase', style: TextStyle(
              color: Colors.white,
              fontSize: 25,
              fontWeight: FontWeight.w900,
            ),
            ),
            backgroundColor: Color(0xFFE28F59),
          )
      ),
    );
  }
}
