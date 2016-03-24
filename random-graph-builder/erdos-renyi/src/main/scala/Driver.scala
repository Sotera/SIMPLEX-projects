import org.apache.spark.{SparkContext, SparkConf}
import org.apache.log4j.{Level, Logger}

object Driver {

  def main(args: Array[String]): Unit = {
    val conf = new SparkConf()
    conf.set("spark.logConf", "true")
    val sc = new SparkContext(conf)
    Logger.getRootLogger.setLevel(Level.WARN)
    val graphGenerator = new ErdosRenyi
    val edgeList = graphGenerator.G(1000, 0.9, sc, 100)

    // for debugging
    val tmp = edgeList.collect()
    tmp.foreach(println)
  }


}


