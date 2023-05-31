import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import SpiritSol from "../components/spiritsol";
import styles from "../styles/Home.module.css";

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <Head>
        <title>Spirit Solutions</title>
        <meta
          name="description"
          content="Generate spiritual reccomendations for your business."
        />
        <link rel="icon" href="/altercall.png" />
      </Head>

      <SpiritSol />
    </div>
  );
};

export default Home;
